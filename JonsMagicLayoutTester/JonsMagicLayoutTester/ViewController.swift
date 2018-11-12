//
//  ViewController.swift
//  JonsMagicLayoutTester
//
//  Created by Jonathan Kopp on 10/25/18.
//  Copyright © 2018 Jonathan Kopp. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    var currentScene = 1
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        one()
    }
    
    
    @IBAction func pressed(_ sender: UIButton) {
        currentScene+=1
        for view in self.view.subviews {
            if(view is UIButton){
                print("My Fav Lil Button")
            }
            else
            {
                view.removeFromSuperview()
            }
        }
        
        
            if(currentScene==1)
            {
                one();
            }
            else if(currentScene == 2)
            {
                two();
            }
            else if(currentScene == 3)
            {
                three();
            }
            else
            {
                currentScene=1
                one();
            }

        
    }
    func one()
    {
        let view1 = UIView(frame: CGRect(x: 0, y: 0, width: view.bounds.width/2-10, height: view.bounds.height))
        view1.backgroundColor = #colorLiteral(red: 0.3647058904, green: 0.06666667014, blue: 0.9686274529, alpha: 1)
        view.addSubview(view1)
        
        let view2 = UIView(frame: CGRect(x: 0, y: view.bounds.height/2, width: view.bounds.width/2-10, height: view.bounds.height/2))
        view2.backgroundColor = #colorLiteral(red: 0.5568627715, green: 0.3529411852, blue: 0.9686274529, alpha: 1)
        view.addSubview(view2)
        
        let view3 = UIView(frame: CGRect(x: view.bounds.width/2+10, y: 0, width: view.bounds.width/2-10, height: view.bounds.height))
        view3.backgroundColor = #colorLiteral(red: 0.3647058904, green: 0.06666667014, blue: 0.9686274529, alpha: 1)
        view.addSubview(view3)
        
        let view4 = UIView(frame: CGRect(x: view.bounds.width/2+10, y: view.bounds.height * 0.25, width: view.bounds.width/2-10, height: view.bounds.height))
        view4.backgroundColor = #colorLiteral(red: 0.5568627715, green: 0.3529411852, blue: 0.9686274529, alpha: 1)
        view.addSubview(view4)
    }
    
    func two()
    {
        let view1 = UIView(frame: CGRect(x: 0, y: 30, width: 150, height: 150))
        view1.backgroundColor = #colorLiteral(red: 0.3647058904, green: 0.06666667014, blue: 0.9686274529, alpha: 1)
        view.addSubview(view1)
        
        let view2 = UIView(frame: CGRect(x: 160, y: 30, width: 150, height: 150))
        view2.backgroundColor = #colorLiteral(red: 0.5568627715, green: 0.3529411852, blue: 0.9686274529, alpha: 1)
        view.addSubview(view2)
    }
    func three()
    {
        let view1 = UIView(frame: CGRect(x: 0, y: 30, width: 150, height: 150))
        view1.backgroundColor = #colorLiteral(red: 0.3647058904, green: 0.06666667014, blue: 0.9686274529, alpha: 1)
        view.addSubview(view1)
        
        //add label name big
        //label2 smaller makeschool
        
    }
    

}

